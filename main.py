import os

class DocumentImporter(object):
    def run(self):
        print '1/3. Importing the following files from OneDrive: %s' % self.scanned_image_files_to_import()

        for file_to_import in self.scanned_image_files_to_import():
            folder_to_import_to = self.choose_file_to_import(file_to_import, self.gdrive_directories())

            one_drive_path_to_file = self.one_drive_path() + '/' + file_to_import
            destination_file_path = self.google_drive_path() + '/' + folder_to_import_to + '/' + file_to_import

            # TODO:
            # make this a recursive function

            full_folder_to_import_to = self.google_drive_path() + '/' + folder_to_import_to
            print "Do you want to move '%s' to '%s'" % (file_to_import, full_folder_to_import_to)
            move_to_current_dir = raw_input()

            if (move_to_current_dir == 'y' or move_to_current_dir == 'yes'):
                print 'Moving %s to %s' % (one_drive_path_to_file, destination_file_path)
                # os.rename(one_drive_path_to_file, destination_file_path)
            else:
                directories = os.listdir(os.path.join(os.path.expanduser("~"), full_folder_to_import_to))
                next_level_dir = self.choose_file_to_import(file_to_import, directories)

                new_destination_path = destination_file_path + '/' + next_level_dir
                print 'Moving %s to %s' % (one_drive_path_to_file, new_destination_path)
                # os.rename(one_drive_path_to_file, new_destination_path)

        print '3/3. Import complete.'

    def choose_file_to_import(self, file_to_import, directories):
        print 'Which folder in GDrive would you like to import "%s"?' % file_to_import
        print directories
        return raw_input()

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
