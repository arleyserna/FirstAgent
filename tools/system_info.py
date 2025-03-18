import platform
import json
import psutil
from smolagents.tools import Tool
from typing import Any, Optional
import webbrowser

class SystemInfo(Tool):

    name = "system_info"
    description = "raise data about the system running the tool."
    inputs = {'query': {'type': 'string', 'description': 'The system data.'}}
    output_type = "string"

    def __init__(self):
        self.is_initialized = False
        self.info = {}

    def collect_info(self):
        self.info['node'] = platform.node()
        self.info['platform'] = platform.system()
        self.info['platform_version'] = platform.version()
        self.info['architecture'] = platform.machine()
        self.info['cpu_count'] = psutil.cpu_count(logical=True)
        self.info['memory'] = psutil.virtual_memory()._asdict()
        self.info['disk'] = psutil.disk_usage('/')._asdict()

    def get_info_as_json(self):
        return json.dumps(self.info, indent=4)
    
    def forward(self, query: str) -> str:
        self.collect_info()
        webbrowser.open('http://localhost:80')
        return self.get_info_as_json()
