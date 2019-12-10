'''
Created by David Ololade Oniku
on June 17, 2019
'''
import numpy as np
import pandas as pd
import datetime
from datetime import datetime
from datetime import timedelta

# filelist = ["2019-02-27_tet0-sl8-ch1_459331_2019-02-27_13-44-34_chart.cht-2019-03-05_19-48-14-707.csv"]
# new_filename = "new.xlsx"

class Tracelogs:
    """
    This program takes two arguments, (1) filelist to reformat and (2)name to save-as the reformatted file.
    The reformatted file will be exported in .xlsx format.

    """
    def __init__(self, filelist, newfile_name, columns_list=[]):
        self.filelist = filelist
        self.newfile_name = newfile_name + ".xlsx"
        self.columns_list = columns_list

    def original_df(self, item):
        original_file = pd.read_csv(item, skiprows=3)
        return original_file

    def is_file_selected(self):
        if len(self.filelist) >= 1:
            return True

    def merge_needed(self):
        if len(self.filelist) > 1:
            return True
        else:
            return False

    def add_to_columns_list(self, new_columns_list):
        self.columns_list.extend(new_columns_list)
        return self.columns_list

    def convert_dropna(self, fileitem):
        DF_file = pd.read_csv(fileitem, skiprows=3)
        DF_file.dropna(axis=0, inplace=True)
        DF_file.reset_index(drop=True, inplace=True)
        return DF_file

    def add_start_date(self, DF):
        global date_string
        date_string = DF.columns[0]
        DF["Start_Date"] = date_string[6:16]
        return DF

    def return_time_string(self, DF):
        global date_string
        date_string = DF.columns[0]
        time_string = date_string[6:17]
        return time_string

    def add_date_time(self, DF):
        DF[date_string] = pd.to_datetime(DF[date_string],
                                         format = '%H:%M:%S.%f')
        DF["DateTime"] = DF[date_string].apply(lambda x: datetime.strftime(x, '%H:%M:%S.%f'))
        return DF

    def format_time(self, DF):
        DF["DateTime"] = DF["DateTime"].apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f'))
        return DF

    def add_elapsed_time(self, DF):
        DF[DF.columns[0]] = pd.to_timedelta(DF[DF.columns[0]], errors='coerce')
        DF['Elapsed_Time_sec'] = (DF[DF.columns[0]].dt.total_seconds() - DF[DF.columns[0]].dt.total_seconds().iloc[0])
        return DF

    def add_sample_index(self, sample, DF):
        str = "sample_{}".format(sample)
        DF['sample_index'] = str
        return DF

    def get_column_header(self, DF):
        DF_head = DF.columns.values
        column_header_DF = pd.DataFrame(DF_head).T
        column_header_DF.columns = column_header_DF.iloc[0, :]
        column_header_DF.drop([0], axis=0, inplace=True)
        return column_header_DF

    def change_column_name(self, DF, index, new_name):
        DF.columns.values[index] = new_name
        return DF

    def merge_file(self, DF, new_DF):
        DF = DF.append(new_DF, ignore_index=False, sort=False)
        return DF

    def reset_index_inplace(self, DF):
        DF.reset_index(drop=False, inplace=True)
        return DF

    def reset_index_drop(self, DF):
        DF.reset_index(drop=True, inplace=True)
        return DF

    def drop_column(self, DF, column_to_drop):
        DF.drop([column_to_drop], axis = 1, inplace = True)
        return DF

    def get_columns_list(self, DF):
        return DF.columns.values

    def export_file(self, DF):
        writer = pd.ExcelWriter(self.newfile_name, engine = "xlsxwriter")
        DF.to_excel(writer, sheet_name='Sheet1')
        return writer.save()
        # return DF.to_excel(self.newfile_name, sheet_name = "Sheet1", engine = "xlsxwriter")

    try:
        def reFormat(self):
            if self.is_file_selected():
                item = self.filelist[0]
                file = self.convert_dropna(item)
                filedate = self.add_start_date(file)
                file_with_time = self.add_date_time(filedate)
                file_elapsed_time = self.add_elapsed_time(file_with_time)
                sample_index = self.filelist.index(item) + 1
                file_sample_index = self.add_sample_index(sample_index, file_elapsed_time)
                columns_header = self.get_column_header(file_sample_index)
                file_merger = self.change_column_name(columns_header, 0, "Time")
                file_merger = self.merge_file(file_merger, file)
                if not self.merge_needed():
                    self.reset_index_drop(file_merger)
                    # return self.export_file(self.drop_column(file_merger, file_merger.columns[0]))
                    return self.drop_column(file_merger, file_merger.columns[0])
                    # return file_merger
                else:
                    for num in range(1, len(self.filelist)):
                        item_b = self.filelist[num]
                        file_b = self.convert_dropna(item_b)
                        filedate_b = self.add_start_date(file_b)
                        file_with_time_b = self.add_date_time(filedate_b)
                        file_elapsed_time_b = self.add_elapsed_time(file_with_time_b)
                        sample_index_b = self.filelist.index(item_b) + 1
                        file_sample_index_b = self.add_sample_index(sample_index_b, file_elapsed_time_b)
                        new_merger = self.change_column_name(file_sample_index_b, 0, "Time")
                        file_merger = self.merge_file(file_merger, new_merger)
                    self.reset_index_drop(file_merger)
                    # return self.export_file(self.drop_column(file_merger, file_merger.columns[0]))
                    return self.drop_column(file_merger, file_merger.columns[0])
                    # return file_merger
            else:
                print("You have not selected a file")
    except PermissionError:
        print("File may still be in use, please close the file and try again")
    except:
        print("Please try again later or contact David Oniku for help")

def main():
    filelist = ["2019-02-27_tet0-sl8-ch1_459331_2019-02-27_13-44-34_chart.cht-2019-03-05_19-48-14-707.csv"]
    newfile_name = "new.xlsx"
    trace_logs = Tracelogs(filelist, newfile_name)
    writer = pd.ExcelWriter(newfile_name, engine="xlsxwriter")
    trace_logs.reFormat().to_excel(writer, sheet_name='Sheet1')
    return writer.save()

    # return trace_logs.reFormat()

if __name__ == "__main__": main()
