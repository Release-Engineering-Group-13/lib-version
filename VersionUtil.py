import os

class VersionUtil:
    @staticmethod
    def get_version():
        try:
            with open('VERSION', 'r') as version_file:
                return version_file.read().strip()
        except FileNotFoundError:
            return "Unknown version"

# Example Usage
print(VersionUtil.get_version())
