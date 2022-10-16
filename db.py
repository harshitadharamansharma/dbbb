class TreeNode:
    def _init_(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode("university")
    Name = TreeNode(" Univerity of Delhi")
    root.add_child(Name)

    ADDRESSUNIVER = TreeNode("Address")
    ADDRESSUNIVER.add_child(TreeNode("Benito_Juarez_Marg"))
    ADDRESSUNIVER.add_child(TreeNode("South Campus"))
    ADDRESSUNIVER.add_child(TreeNode("DELHI"))
    ADDRESSUNIVER.add_child(TreeNode("New_DELHI"))
    ADDRESSUNIVER.add_child(TreeNode("India"))

    root.add_child(ADDRESSUNIVER)









    ViceChancellor = TreeNode("ViceChancellor")
    ViceChancellor.add_child(TreeNode("Prof. P.C Joshi"))
    ViceChancellor.add_child(TreeNode("8826156303"))
    ViceChancellor.add_child(TreeNode("Joshi@du.ac.in"))
    root.add_child(ViceChancellor)

    ADDRESSVC = TreeNode("Address")
    ADDRESSVC.add_child(TreeNode("Benito_Juarez_Marg"))
    ADDRESSVC.add_child(TreeNode("Motibagh"))
    ADDRESSVC.add_child(TreeNode("DELHI"))
    ADDRESSVC.add_child(TreeNode("New_DELHI"))
    ADDRESSVC.add_child(TreeNode("India"))
    ViceChancellor.add_child(ADDRESSVC)


    Dean1 = TreeNode("Dean1")
    Dean1.add_child(TreeNode("NameOfFaculty"))
    Dean1.add_child(TreeNode("Name"))
    Dean1.add_child(TreeNode("ContactNumber"))
    Dean1.add_child(TreeNode("EmailID"))
    Dean1.add_child(TreeNode("EmployeeID"))


    ADDRESSDean1 = TreeNode("Address")
    ADDRESSDean1.add_child(TreeNode("Benito_Juarez_Marg"))
    ADDRESSDean1.add_child(TreeNode("Motibagh"))
    ADDRESSDean1.add_child(TreeNode("DELHI"))
    ADDRESSDean1.add_child(TreeNode("New_DELHI"))
    ADDRESSDean1.add_child(TreeNode("India"))


    Dean1.add_child(ADDRESSDean1)
    ViceChancellor.add_child(Dean1)
    Departments = TreeNode("Departments")
    DepartmentsDetails_1=TreeNode("DepartmentsDetails_1")
    DepartmentsDetails_1.add_child(TreeNode("DepartmentName"))
    DepartmentsDetails_1.add_child(TreeNode("Head_of_the_Department"))
    DepartmentsDetails_1.add_child(TreeNode("Name"))
    DepartmentsDetails_1.add_child(TreeNode("ContactNumber"))
    DepartmentsDetails_1.add_child(TreeNode("EmailID"))
    Departments.add_child(DepartmentsDetails_1)



   
    root.print_tree()

# if _name_ == '_main_':
#     build_product_tree()