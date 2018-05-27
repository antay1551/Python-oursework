import unittest
import Anton_Tolok_KC22
 
class Test(unittest.TestCase):
    def test_drop_sumbols(self):
        self.assertEqual(Anton_Tolok_KC22.drop_sumbols(['.together', 'as:', 'though.', ':ships', 'imperial;']), ['together', 'as', 'though', 'ships', 'imperial'])
    def test_uniq_elements(self):
       self.assertEqual(Anton_Tolok_KC22.uniq_elements(['to', 'to', 'to', 'think', 'think', 'about']), ['about', 'think', 'to'])
    def test_search_key_1(self):
       self.assertEqual(Anton_Tolok_KC22.search_key_to_unit_test( ['there', 'top', 'my'], 10), 0 )
    def test_search_key_2(self):
       self.assertEqual(Anton_Tolok_KC22.search_key_to_unit_test( ['there', 'top', 'my'], 1), 1 )
    def test_split_file(self):
       self.assertEqual(Anton_Tolok_KC22.split_file( '.to my mind there is no time to loze it.'), ['.to', 'my', 'mind', 'there', 'is', 'no', 'time', 'to', 'loze', 'it.'] )
if __name__ == '__main__':
    unittest.main()
