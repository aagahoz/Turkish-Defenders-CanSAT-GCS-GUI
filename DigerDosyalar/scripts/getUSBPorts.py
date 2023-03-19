import subprocess

command = "system_profiler SPUSBDataType"
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

if error:
    print(f"Error: {error.decode('utf-8')}")
else:
    usb_list = output.decode('utf-8').split('\n\n')[1:-1]
    for usb_device in usb_list:
        name = usb_device.split('\n')[0].strip()
        print(name)
