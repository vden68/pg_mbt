__author__ = 'vden'

from fixture.fixdb.connect import ConnectHelper



class Dbfixture:

    def __init__(self, mbt_hosts_write, mbt_hosts_read):
        self.mbt_hosts_write = mbt_hosts_write
        self.mbt_hosts_read = mbt_hosts_read

        self.conn = ConnectHelper(self)

    """

    def get_group_list(self, clean=False):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                if clean :
                    list.append(Group(id=str(id), name=name.strip(), header=header, footer=footer))
                else:
                    list.append(Group(id=str(id), name=name, header=header, footer=footer))

        finally:
            cursor.close()
        return list

    def get_contact_list(self, clean=False):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname "
                           "from addressbook "
                           "where deprecated= '0000-00-00 00'")
            for row in cursor:
                (id, firstname, lastname) = row
                if clean :
                    list.append(Contact(id=str(id), firstname=firstname.strip(), lastname=lastname.strip()))
                else:
                    list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list
        
    """

    def destroy(self):
        pass
        #self.connection.close()



