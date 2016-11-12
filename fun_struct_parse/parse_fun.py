from __future__ import print_function
import sys
sys.path.extend(['.', '..'])
from pycparser import c_ast, parse_file

class FuncDefVisitorPointer(c_ast.NodeVisitor):
    def visit_FuncDef(self, node):
        for (child_name, child) in node.children(): #Go to all child
            flag = 0
            for params in (node.decl.type.args.params): #Go to all type parametrs
                if type(params.type.type) is c_ast.Struct: #Verify type is params, if Struct- go to if
                    flag = 1
                    print(node.coord, "In function struct ,without pointer value: ",params.type.type.name)
            if flag == 1:
                    break
def show_func_defs(filename):
    ast = parse_file(filename, use_cpp=True,
                     cpp_args=r'-Iutils/fake_libc_include')
    v = FuncDefVisitorPointer() #Call Visiter to node
    v.visit(ast)                #Pass to parametr our filename

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename  = sys.argv[1]
        print("\n",filename)
    else:
        filename = 'a.c'
    show_func_defs(filename)
