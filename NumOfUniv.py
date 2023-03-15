from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure, show
from bokeh.transform import factor_cmap
import csv
def GenerateBarGraphUniversity(DataFile): 
        CSVdata = []
        for i in range(18):
                CSVdata.append([])
        with open(DataFile,'r') as csvfile:
                lines = csv.reader(csvfile, delimiter=',')
                for row in lines:
                        for i in range(1, 19):
                                CSVdata[i - 1].append(row[i])
        
        Courses = []
        for i in range(18):
                Courses.append(CSVdata[i][0])
        SchoolType = ['UCs', 'CSUs']
        data = {}
        data['Courses'] = Courses
        data['UCs'] = []
        data['CSUs'] = []
        for i in range(18):
                data['UCs'].append((float(CSVdata[i][1]) / 8) * 100)
                
                data['CSUs'].append((float(CSVdata[i][2]) / 5) * 100)
        # data = {'fruits' : fruits,
        #         '2015'   : [2, 1, 4, 3, 2, 4],
        #         '2016'   : [5, 3, 3, 2, 4, 6],
        #         '2017'   : [3, 2, 4, 4, 5, 3]}

        palette = ["#c9d9d3", "#718dbf", "#e84d60"]

        # this creates [ ("Apples", "2015"), ("Apples", "2016"), ("Apples", "2017"), ("Pears", "2015), ... ]
        x = [ (course, school) for course in Courses for school in SchoolType ]
        counts = sum(zip(data['UCs'], data['CSUs']), ()) # like an hstack

        source = ColumnDataSource(data=dict(x=x, counts=counts))

        p = figure(x_range=FactorRange(*x), height=500, width=3000,  title="Percentage of UCs vs CSUs that Require Courses",
                toolbar_location=None, tools="")

        p.vbar(x='x', top='counts', width=.75, source=source, line_color="white",
        fill_color=factor_cmap('x', palette=palette, factors=SchoolType, start=1, end=2))
        p.y_range.start = 0
        p.x_range.range_padding = 0.05
        p.xaxis.major_label_orientation = 1
        p.xgrid.grid_line_color = None
        show(p)

GenerateBarGraphUniversity('numOfUnivAdm.csv')