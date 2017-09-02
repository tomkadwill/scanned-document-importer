import os

class DocumentImporter(object):
    def run(self):
        print '1/3. Importing the following files from OneDrive: %s' % self.scanned_image_files_to_import()

        for file_to_import in self.scanned_image_files_to_import():
            print '2/3. Which folder in GDrive would you like to import "%s"?' % file_to_import
            print self.gdrive_directories(),
            folder_to_import_to = raw_input()

            one_drive_path_to_file = self.one_drive_path() + '/' + file_to_import
            destination_file_path = self.google_drive_path() + '/' + folder_to_import_to + '/' + file_to_import

            print 'Moving %s to %s' % (one_drive_path_to_file, destination_file_path)
            os.rename(one_drive_path_to_file, destination_file_path)

        print '3/3. Import complete.'

    def files_to_import(self):
        return [f for f in os.listdir(self.one_drive_path()) if os.path.isfile(os.path.join(self.one_drive_path(), f))]

    def gdrive_directories(self):
        return os.listdir(os.path.join(os.path.expanduser("~"), self.google_drive_path()))

    def scanned_image_files_to_import(self):
        files = []
        for file_name in self.files_to_import():
            if file_name.endswith('.pdf') or file_name.endswith('png'):
                files.append(file_name)

        return files

    def one_drive_path(self):
        return os.path.join(os.path.expanduser("~"), 'OneDrive')

    def google_drive_path(self):
        return os.path.join(os.path.expanduser("~"), 'Google Drive')

if __name__ == '__main__':
    DocumentImporter().run()
