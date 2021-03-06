import os
import glob
import datetime
import pandas as pd
from cgl.core.util import cgl_copy
from plugins.preflight.preflight_check import PreflightCheck
from cgl.core.path import PathObject, CreateProductionData, split_sequence, split_sequence_frange

FILEPATH = 0
FILENAME = 1
FILETYPE = 2
FRANGE = 3
TAGS = 4
KEEP_CLIENT_NAMING = 5
SCOPE = 6
SEQ = 7
SHOT = 8
TASK = 9
PUBLISH_FILEPATH = 10
PUBLISH_DATE = 11
STATUS = 12


class CreatePublishFiles(PreflightCheck):
    """
    This Class is designed specifically to work with the lumbermill ingest tool.  It expects a lumbermill data frame in order to function.

    """

    def __init__(self):
        self.pandas_path = self.shared_data['pandas_path']
        self.data_frame = self.shared_data['data_frame'].copy(deep=True)
        self.test = False

    def getName(self):
        pass

    def make_source_file(self, to_path, row):
        source_path = PathObject(to_path)
        source_path.set_attr(context='source')
        source_path.set_attr(filename='system_report.csv')
        dir = os.path.dirname(source_path.path_root)
        data = []
        data.append((row["Filepath"], row["Filename"], row["Filetype"], row["Frame_Range"], row["Tags"],
                     row["Keep_Client_Naming"], row["Scope"], row["Seq"], row["Shot"], row["Task"],
                     row["Publish_Filepath"], row["Publish_Date"], row["Status"]))
        df = pd.DataFrame(data, columns=self.shared_data['ingest_browser_header'])
        if not self.test:
            df.to_csv(source_path.path_root, index=False)

    def save_data_frame(self):
        print 'saving data to: %s' % self.pandas_path
        self.data_frame.to_csv(self.pandas_path, index=False)

    def run(self):
        d = datetime.datetime.today()
        current_date = d.strftime('%d-%m-%Y %H:%M:%S')
        # This is publishing EVERYTHING, what about the scenario when we don't want that?
        # can i get the selected row only?
        for index, row in self.data_frame.iterrows():
            print index, row
            if row['Status'] == 'Tagged':
                from_file = row['Filepath']
                to_file = row['Publish_Filepath']

                # What to do if it's a Folder
                if row['Filetype'] == 'folder':
                    print 'Copying %s to %s' % (from_file, to_file)
                    # Send this to the Preflights - No matter what basically
                    if not self.test:
                        cgl_copy(from_file, to_file)
                        CreateProductionData(to_file, json=True)
                    self.shared_data['file_tree'].model.item(index, STATUS).setText('Published')
                    self.signal_one.emit([index, STATUS, 'Published'])
                    self.data_frame.at[index, 'Status'] = 'Published'
                    self.data_frame.at[index, 'Publish_Date'] = current_date
                    row['Publish_Date'] = current_date
                    row['Status'] = 'Published'
                    self.make_source_file(to_file, row)

                # What to do with Sequences:
                else:
                    to_dir = os.path.dirname(to_file)
                    if row['Filetype'] == 'sequence':
                        print '2, Sequence'
                        if not self.test:
                            print 'Creating Directory: %s' % to_dir
                            CreateProductionData(to_dir)
                        file_sequence, self.shared_data['frange'] = split_sequence_frange(from_file)
                        from_query = split_sequence(from_file)
                        from_filename = os.path.split(file_sequence)[-1]
                        self.shared_data['published_seq'] = os.path.join(to_dir, from_filename)

                        for f in glob.glob('%s*' % from_query):
                            to_file = os.path.join(to_dir, os.path.basename(f))
                            print 'Copying %s to %s' % (f, to_file)
                            if not self.test:
                                cgl_copy(f, to_file)
                            self.shared_data['file_tree'].model.item(index, STATUS).setText('Published')
                            self.data_frame.at[index, 'Status'] = 'Published'
                            self.data_frame.at[index, 'Publish_Date'] = current_date
                            row['Publish_Date'] = current_date
                            row['Status'] = 'Published'
                            self.make_source_file(to_dir, row)
                    else:
                        print '4 File'
                        print 'Copying %s to %s' % (from_file, to_file)
                        if not self.test:
                            print 'Creating File: %s' % to_file
                            CreateProductionData(os.path.dirname(to_file), json=True)
                            cgl_copy(from_file, to_file)
                        self.shared_data['file_tree'].model.item(index, STATUS).setText('Published')
                        self.data_frame.at[index, 'Status'] = 'Published'
                        self.data_frame.at[index, 'Publish_Date'] = current_date
                        row['Publish_Date'] = current_date
                        row['Status'] = 'Published'
                        self.make_source_file(to_file, row)
                self.shared_data['publish_file'] = to_file
                print('Published Sequence %s' % to_file)
                self.save_data_frame()
                self.pass_check('Check Passed')
            else:
                print 'Skipping Untagged assets'

