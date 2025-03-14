# import module
import platform

# displaying platform processor 
print('Platform processor:', platform.processor())
# output - Platform processor: Intel64 Family 6 Model 154 Stepping 4, GenuineIntel

# displaying platform architecture 
print('Platform architecture:', platform.architecture()) 

# displaying machine type 
print('Machine type:', platform.machine())

# displaying system network name 
print("System's network name:", platform.node())

# displaying platform information 
print('Platform information:', platform.platform())

# displaying platform processor name 
print('Platform processor:', platform.processor())

# displaying OS name 
print('Operating system:', platform.system())

# displaying system info 
print('System info:', platform.uname())

# displaying python build date and no.
print('Python build no. and date:', platform.python_build())


# displaying python compiler 
print('Python compiler:', platform.python_compiler()) 

# displaying python SCM info 
print('Python SCM:', platform.python_branch())

# displaying python implementation 
print('Python implementation:', platform.python_implementation())

# displaying python version 
print('Python version:', platform.python_version())

# displaying version 
print('Version:', platform.version())

# displaying python version tuple
print('Python Version Tuple:', platform.python_version_tuple() )
