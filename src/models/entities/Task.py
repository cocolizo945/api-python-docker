from utils.DateFormat import DateFormat


class Task():

    def __init__(self, id, taskname=None, template=None, range_start=None, 
                 range_end=None, status=None, description=None, repeat_task = None, level_task = None) -> None:
        self.id          = id
        self.taskname    = taskname
        self.template    = template
        self.range_start = range_start
        self.range_end   = range_end
        self.status      = status
        self.description = description
        self.repeat_task = repeat_task
        self.level_task  = level_task
        

    def to_JSON(self):
        return {
            'id'            : self.id,         
            'taskname'      : str(self.taskname), 
            'template'      : self.template,   
            'range_start'   : str(self.range_start),
            'range_end'     : str(self.range_end),
            'status'        : self.status,     
            'description'   : str(self.description),
            'repeat_task'   : self.repeat_task,
            'level_task'    : self.level_task 
        }