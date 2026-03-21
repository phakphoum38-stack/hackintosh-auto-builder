from core.hardware_scanner import scan_hardware
from core.cpu_patcher import patch_cpu
from core.gpu_patcher import patch_gpu
from core.config_generator import generate_config
from core.efi_builder import build_efi
from downloader.kext_downloader import get_kexts

def main():

    print("Hackintosh Auto Builder")

    hw = scan_hardware()

    cpu_patch = patch_cpu(hw)
    gpu_patch = patch_gpu(hw)

    kexts = get_kexts()

    config = generate_config(
        hw,
        cpu_patch,
        gpu_patch,
        kexts
    )

    build_efi(config, kexts)

    print("EFI build complete")

if __name__ == "__main__":
    main()
