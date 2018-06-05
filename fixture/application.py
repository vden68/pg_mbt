__author__ = 'vden'


class Application:

    def __init__(self, mbt_hosts, mbt_hosts_write, mbt_hosts_read, mbt_conn):

        self.mbt_hosts = mbt_hosts
        self.mbt_hosts_write = mbt_hosts_write
        self.mbt_hosts_read = mbt_hosts_read
        self.mbt_conn = mbt_conn

        """
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" %browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.navigation = NavigationHelper(self)
        self.common = CommonHelper(self)
        self.base_url = base_url
        """
"""
    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()

    def clear_contact(self, s):
        return re.sub("[( )-]", "",s)

    def merge_phones_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != " " ,
                                (map(lambda x: self.clear_contact(x),
                                     (filter(lambda x: x is not None,
                                             [contact.homephone, contact.mobilephone,
                                              contact.workphone, contact.seconderyphone]))))))
"""






