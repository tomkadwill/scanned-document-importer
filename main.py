import os

ONE_DRIVE_PATH = '/Users/thomaskadwill/OneDrive'
GDRIVE_PATH = '/Users/thomaskadwill/Google Drive'

def main():
    print '1/4. Scanning OneDrive for new scanned files'
    files_to_import = [f for f in os.listdir(ONE_DRIVE_PATH) if os.path.isfile(os.path.join(ONE_DRIVE_PATH, f))]

    gdrive_directories = os.listdir(GDRIVE_PATH)

    scanned_image_files_to_import = []
    for file_name in files_to_import:
        if file_name.endswith('.pdf') or file_name.endswith('png'):
            scanned_image_files_to_import.append(file_name)

    print '2/4. Importing the following files: %s' % scanned_image_files_to_import

    for file_to_import in scanned_image_files_to_import:
        print '3/4. Which folder in GDrive would you like to import "%s"?' % file_to_import
        print gdrive_directories,
        folder_to_import_to = raw_input()

        one_drive_path_to_file = ONE_DRIVE_PATH + '/' + file_to_import
        destination_file_path = GDRIVE_PATH + '/' + folder_to_import_to + '/' + file_to_import

        print 'Moving %s to %s' % (one_drive_path_to_file, destination_file_path)
        os.rename(one_drive_path_to_file, destination_file_path)

    print '4/4. Import complete.'

if __name__ == '__main__':
    main()
