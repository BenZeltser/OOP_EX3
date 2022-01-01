from DiGraph import DiGraph
import unittest

class TestDiGrapgh(unittest.TestCase):

    def setUp(self):
        self.g= DiGraph()
        for x in range (4):
            self.g.add_node(x)
        self.g.add_edge(0, 1, 1)
        self.g.add_edge(1, 0, 1.1)
        self.g.add_edge(1, 2, 1.3)



    def test_v_size(self):
        self.assertEqual(self.g.v_size(),4)

    def test_edge_size(self):
        self.assertEqual(self.g.e_size(),3)

    def test_get_all_v(self):
        self.assertEqual(len(self.g.get_all_v()),self.g.v_size())

    def test_all_in_edges_of_node(self):
        self.assertEqual(len(self.g.all_in_edges_of_node(1)),1)

    def test_out_edges_of_node(self):
        self.assertEqual(len(self.g.all_in_edges_of_node(1)), 2)

    def test_get_mc(self):
        self.assertEqual(7,self.g.get_mc)

    def test_add_edge(self):
        self.assertEqual(self.g.add_edge(0,1,1),False)
        self.assertEqual(self.g.add_edge(2,1,1.2),True)

    def test_add_node(self):
        self.assertEqual(self.g.add_node(2),False)
        self.assertEqual(self.g.add_node(5), True)

    def test_remove_node(self):
        self.assertEqual(self.g.remove_node(2),True)
        self.assertEqual(self.g.remove_node(7),False)

    def test_remove_edge(self):
        self.assertEqual(self.g.remove_edge(0,1),True)
        self.assertEqual(self.g.remove_edge(1,4),False)

if __name__ == '__main__':
    unittest.main()



