#coding=utf-8
import os,time,threading
import sys
all_file_list = []
sp_list_c = []
grep_context = ""
def visit_folder_files(arg,dirname,names):
	# all_file_list = []
	for filepath in names:
		mtr = os.path.join(dirname,filepath)
		if os.path.isfile(mtr):
			all_file_list.append(mtr)

def search_all_folder_files(path):
	os.path.walk(path,visit_folder_files,())

def splist(l,s):
	return [l[i:i+s] for i in range(len(l)) if i%s==0]

def grep_action(arg):
	import commands
	grep_file_list = sp_list_c[arg]
	for filename in grep_file_list:
		cmd_str = "grep -nb "%s" %s" % (grep_context,filename)
		os_result = commands.getoutput(cmd_str)
		if len(os_result) > 0 :
			print "file name %s " % filename
			print os_result
			print "\n"

def multi_threading_grep_enter(pieces):
	for i in range(0,pieces):
		grep_t = threading.Thread(target=grep_action,args=(i,))
		grep_t.start()

if __name__ == '__main__':
	search_all_folder_files(sys.argv[3])
	file_list_length = len(all_file_list)
	file_l = file_list_length / (int)(sys.argv[1])
	grep_context = sys.argv[2]
	sp_list_c = splist(all_file_list,file_l)
	multi_threading_grep_enter((int)(sys.argv[1]))
	
	
