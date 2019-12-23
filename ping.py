import subprocess

class Ping:
    def __init__(self, platform: str , uri: str, count: str):
        self.uri = uri
        self.platform = platform
        if platform == 'Darwin':
            self.command = ['ping', '-c', count, uri]
        elif platform == 'Windows':
            self.command = ['ping', '-n', count, uri]
    
    def __repr__(self):
        return ' '.join(self.command)

    def _avg_from_result_keywords(self, results):
        if self.platform == 'Darwin':
            speeds = results.split('min/avg/max/stddev = ')
            avg = speeds[1].split('/')[1]
            return float(avg)
        elif self.platform == 'Windows':
            avg = results.split('Average = ')
            return float(avg[1][:-2])

    def send(self):
        cmd = subprocess.run(
            self.command,
            stdout=subprocess.PIPE
        )
        return '{}: {}'.format(self.uri, cmd.stdout.splitlines()[-1].decode('utf-8'))

    def average(self, results):
        return self._avg_from_result_keywords(results)