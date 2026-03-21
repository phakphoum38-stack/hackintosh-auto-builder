import os
import shutil

def build_efi(config, kexts):

    base = "output/EFI/OC"

    os.makedirs(base + "/Kexts", exist_ok=True)
    os.makedirs(base + "/ACPI", exist_ok=True)
    os.makedirs(base + "/Drivers", exist_ok=True)

    for k in kexts:

        path = base + "/Kexts/" + k

        open(path, "w").close()

    shutil.copy(
        "output/config.plist",
        base + "/config.plist"
    )
