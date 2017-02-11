'''
    The UI runner script for the Booth's Multiplication Api.
    *******************************************************
    ** @required
    ** 1.) python2.7
    ** 2.) Bottle framework
    *******************************************************
    *******************************************************

    #codedByBotman
'''

from bottle import Bottle, run, template, request, static_file
from Models.BusinessLogic.BoothMultiplier import * # The botman's api for Booth Multiplication

botApp = Bottle() # create a bottle application object to run the application

# static route to serve the js and css files
@botApp.route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

# default route to land in when the application is started
@botApp.get('/')
def shower():
    return template("home")

# The route that serves the actual multiply request.
@botApp.get('/multiply')
def boothM():
    num1 = int(request.params['num1'])
    num2 = int(request.params['num2'])

    return template("home",
        ans = reduce(
                lambda x, y: x + y, # the reduction function to be applied
                map(str, BoothMultiplier.multiply(BitNibbles(num1), BitNibbles(num2)))
        )
    )

# run the application on localhost and port
run(botApp, # the application that is to be run
    host = "localhost", # the host for the application
    port = 6969 # the port number on which the application will run
)
