class Entry:
    def __init__(self, hostname, ip, flag):
        # self._entryList = []

        # ensure hostname is in all lowercase
        hostname = hostname.lower()

        # set values
        self._entrylist = [hostname, ip, flag]
        # self._hostname = hostname
        # self._ip = ip
        # self._flag = flag

    @property
    def entrylist(self):
        return self._entrylist

    # @property
    # def hostname(self):
    #     return self._hostname

    # @property
    # def ip(self):
    #     return self._ip

    # @property
    # def flag(self):
    #     return self._flag

    def to_string(self):
        return "{} {} {}".format(self._entrylist[0], self._entrylist[1], self._entrylist[2])


class Table:
    def __init__(self):
        self._a_records = []
        self._ns_record = None

    def lookup(self, hostname):
        # ensure hostname is in all lowercase
        hostname = hostname.lower()

        for entry in self._a_records:
            if entry.entrylist[0] == hostname:
                return entry

        return self._ns_record

    def add(self, entry_to_add):
        if entry_to_add.entrylist[2] == 'A':
            self._a_records.append(entry_to_add)
        else:
            self._ns_record = entry_to_add
