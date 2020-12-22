import os
import requests
from bs4 import BeautifulSoup
import platform
from shutil import copyfile


def get_platform():
    return platform.system()


def get_ip(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    ip = soup.select("ul.comma-separated > li")[0].text
    print(ip)
    return ip


def append_hosts(append):
    hosts_target_file = open("hosts", "a")
    hosts_target_file.write("\n" + append)


def init_hosts(system):
    hosts_target_file = open("hosts", "w+")
    hosts_template_file = open("template\\hosts_" + system, "r")
    hosts_target_file.write(hosts_template_file.read())


def scan_files(directory,prefix=None,postfix=None):
    files_list=[]
    
    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root,special_file))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(root,special_file))
            else:
                files_list.append(os.path.join(root,special_file))
                          
    return files_list


def copy_host(system):
    if system == "Windows":
        try:
            copyfile("hosts", "C:\\Windows\\System32\\drivers\\etc\\hosts")
            print("Copied to C:\\Windows\\System32\\drivers\\etc\\hosts")
        except IOError as e:
            print("Unable to copy file. %s" % e)
            exit(1)
        except:
            print("Unexpected error:", sys.exc_info())
            exit(1)
    elif system in ["Linux", "Darwin"] :
        try:
            copyfile("hosts", "\\etc\\hosts")
            print("Copied to \\etc\\hosts")
        except IOError as e:
            print("Unable to copy file. %s" % e)
            exit(1)
        except:
            print("Unexpected error:", sys.exc_info())
            exit(1)


def flush_dns(system):
    if system == "Windows":
        os.system("ipconfig /flushdns")
    elif system in ["Linux", "Darwin"]:
        os.system("sudo /etc/init.d/networking restart")


def handle_plugins():
    file_list = get_file_list()
    for file in file_list:
        os.system("python " + file)


def get_file_list():
    file_list = scan_files("plugins", "plugin_")
    print(file_list)
    return file_list