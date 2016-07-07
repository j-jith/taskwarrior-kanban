import subprocess
import json
import jinja2

MAX_COMPLETED = 10 # max. no. of completed tasks to display

def get_tasks(tags):

    # run taskwarrior export
    command = ['task', 'rc.json.depends.array=no', 'export'] + tags 
    data = subprocess.check_output(command) 
    data = data.decode('utf-8') # decode bytestring to string
    data = data.replace('\n','') # remove newline indicators

    # load taskwarrior export as json data
    tasks = json.loads(data)

    return tasks

def render_template(tasks_dic):

    # jinja stuff to load template
    template_loader = jinja2.FileSystemLoader(searchpath='./')
    template_env = jinja2.Environment(loader=template_loader)
    template_file = 'template.jinja'
    template = template_env.get_template(template_file)

    # render template and return html
    return template.render(tasks_dic)    

def write_html(data, filename):

    # write data to file
    with open(filename, 'w') as f:
        f.write(data)

if __name__ == '__main__':

    # empty dictionary to be filled up and passed to jinja template rendering function
    tasks_dic = {} 

    # get pending tasks
    pending_tasks = get_tasks(['status:pending'])
    # add pending tasks to dictionary
    tasks_dic['pending_tasks'] = [task['description'] for task in pending_tasks]

    # get completed tasks and add to dictionary
    completed_tasks =get_tasks(['status:completed']) 
    tasks_dic['completed_tasks'] = [task['description'] for task in completed_tasks[:MAX_COMPLETED-1]]

    # pass dictionary to render template and get html
    html = render_template(tasks_dic)

    # write html to file
    write_html(html, 'index.html')
