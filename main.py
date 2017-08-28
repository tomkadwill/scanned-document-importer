import os

def main():
    print '1/3. Scanning OneDrive for new scanned files'
    one_drive_path = '/Users/thomaskadwill/OneDrive'
    files_to_import = [f for f in os.listdir(one_drive_path) if os.path.isfile(os.path.join(one_drive_path, f))]

    gdrive_path = '/Users/thomaskadwill/Google Drive'
    gdrive_directories = os.listdir(gdrive_path)

    scanned_image_files_to_import = []
    for file_name in files_to_import:
        if file_name.endswith('.pdf') or file_name.endswith('png'):
            scanned_image_files_to_import.append(file_name)

    print '2/3. Importing the following files: %s' % scanned_image_files_to_import

    for file_to_import in scanned_image_files_to_import:
        print '3/3. Which folder in GDrive would you like to import "%s"?' % file_to_import
        print gdrive_directories,
        folder_to_import_to = raw_input()

        one_drive_path_to_file = one_drive_path + '/' + file_to_import
        destination_file_path = gdrive_path + '/' + folder_to_import_to + '/' + file_to_import

        print 'Moving %s to %s' % (one_drive_path_to_file, destination_file_path)
        os.rename(one_drive_path_to_file, destination_file_path)

if __name__ == '__main__':
    main()
