from advanced_console.schemes import BaseNode, ClassicVerticalTree

branch_root = BaseNode("Change 'release_1.0'", color="green")

branch_1 = BaseNode("DB 'test_db' (192.168.0.34)", color="cyan")
branch_1.add(BaseNode("clear_last_release_cache.sql"))
branch_1.add(BaseNode("init_table.sql"))

branch_2 = BaseNode("DB 'test2_db' (16.14.65.77)", color="cyan")
branch_2.add(BaseNode("zero_point_module.sql"))

branch_root.add(branch_1)
branch_root.add(branch_2)

tree = ClassicVerticalTree(root_node=branch_root)

tree.display()
# tree.save_on_file(filename="./scheme_example.txt")
