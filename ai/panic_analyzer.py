def analyze_log(log):

    if "ACPI Error" in log:

        return "ACPI patch required"

    if "GPU Panic" in log:

        return "GPU configuration problem"

    if "AppleIntelCPUPowerManagement" in log:

        return "CPU power management issue"

    return "Unknown error"
