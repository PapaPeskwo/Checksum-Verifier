import subprocess
import platform
import os
import time
import tkinter as tk
from tkinter import filedialog


def generate_sha1(filename):
    if platform.system() == "Windows":
        sha1 = subprocess.check_output(["certutil", "-hashfile", filename, "SHA1"]).split()[-6]
    else:
        sha1 = subprocess.check_output(["sha1sum", filename]).split()[0]
    sha1 = sha1.decode("utf-8").rstrip()
    return sha1

def generate_sha256(filename):
    if platform.system() == "Windows":
        sha256 = subprocess.check_output(["certutil", "-hashfile", filename, "SHA256"]).split()[-6]
    else:
        sha256 = subprocess.check_output(["sha256sum", filename]).split()[0]
    sha256 = sha256.decode("utf-8").rstrip()
    return sha256

def generate_sha512(filename):
    if platform.system() == "Windows":
        sha512 = subprocess.check_output(["certutil", "-hashfile", filename, "SHA512"]).split()[-6]
    else:
        sha512 = subprocess.check_output(["sha512sum", filename]).split()[0]
    sha512 = sha512.decode("utf-8").rstrip()
    return sha512

def generate_md5(filename):
    if platform.system() == "Windows":
        md5 = subprocess.check_output(["certutil", "-hashfile", filename, "MD5"]).split()[-6]
    else:
        md5 = subprocess.check_output(["md5sum", filename]).split()[0]
    md5 = md5.decode("utf-8").rstrip()
    return md5

def compare_hashes(filename, known_hash, hash_function):
    file_hash = hash_function(filename)
    print(f"\nKnown hash value: {known_hash}")
    print(f"File hash value: {file_hash}")
    if file_hash == known_hash:
        print()
        print('+' + '=' * 98 + '+')
        print(f"The file: \n{filename} \nis authentic.")
        print('+' + '=' * 98 + '+')
    else:
        print()
        print('!!!' + '=' * 94 + '!!!')
        print(f"THE FILE: \n{filename} \nMAY HAVE BEEN TAMPERED WITH.")
        print('!!!' + '=' * 94 + '!!!')
    input("\nPress Enter to return to menu.")

def open_file_dialog(known_hash, hash_function):
    filename = filedialog.askopenfilename()
    compare_hashes(filename, known_hash, hash_function)

def hash_sha1():
    known_hash = input("\nEnter the known SHA-1 hash value:\n").lower().strip()
    open_file_dialog(known_hash, generate_sha1)

def hash_sha256():
    known_hash = input("\nEnter the known SHA-256 hash value:\n").lower().strip()
    open_file_dialog(known_hash, generate_sha256)

def hash_sha512():
    known_hash = input("\nEnter the known SHA-512 hash value:\n").lower().strip()
    open_file_dialog(known_hash, generate_sha512)

def hash_md5():
    known_hash = input("\nEnter the known MD5 hash value:\n").lower().strip()
    open_file_dialog(known_hash, generate_md5)

# Menu
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nHash Comparison")
    print("Select a hash function")
    print("1. MD5")
    print("2. SHA1")
    print("3. SHA256")
    print("4. SHA512")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == '1':
        hash_md5()
    elif choice == '2':
        hash_sha1()
    elif choice == '3':
        hash_sha256()
    elif choice == '4':
        hash_sha512()
    elif choice == '5':
        print("Exiting.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
        time.sleep(2)
