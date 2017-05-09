from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem
import datetime
import cgi

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/restaurants"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                restaurants = session.query(Restaurant.name, Restaurant.id).order_by(Restaurant.name.asc()).all()
                output = ""
                output += "<h1><a href='/restaurants/new'>Enter a new restraunt </a></h1>"
                output += "<html><body>"
                for restaurant in restaurants:
                    name = restaurant[0]
                    id = restaurant[1]
                    output += "<h1> %s </h1>" % name
                    output += "<a href='restaurants/%s/edit'>Edit</a> <a href='restaurants/%s/delete'>Delete</a>" % (id, id)
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return
            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""

                output += "<html><body><h1>Welcome to the Restraunt adder</h1>"
                output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/new'><h2>Please add a new restraunt below</h2><input name='newrestraunt' type='text' ><input type='submit' value='Create'> </form>"
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return
            if self.path.endswith("/edit"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                restrauntIDPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(id=restrauntIDPath). one()
                if myRestaurantQuery != []:

                    output = ""

                    output += "<html><body><h1>Please update %s</h1>" % myRestaurantQuery.name
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/edit'>" % restrauntIDPath
                    output += "<input name='updaterestraunt' type='text' placeholder='%s'>" %myRestaurantQuery.name
                    output += "<input type='submit' value='Rename'> </form>"
                    output += "</body></html>"
                    self.wfile.write(output)
                    print output
                return
        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)

    def do_POST(self):
        try:
            self.send_response(301)
            self.end_headers()

            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                newrestaurantname = fields.get('newrestraunt')
            output = ""
            output += "<html><body>"
            output += "<h2> The following restraunt has been added, thank you! </h2>"
            output += "<h1> %s </h1>" % newrestaurantname[0]
            output += "<h4> Would you like to enter another? </h2>"
            output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/new'><h2>Please add a new restraunt below</h2><input name='newrestraunt' type='text' ><input type='submit' value='Create'> </form>"
            output += "<a href='/restaurants'> Return to the home page </a>"
            output += "</body></html>"
            self.wfile.write(output)
            addNewRestraunt = Restaurant(name=newrestaurantname[0])
            session.add(addNewRestraunt)
            session.commit()
            print output
            return
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                restrauntIDPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(id=restrauntIDPath). one()
                restaurantname = fields.get('updaterestraunt')

                output = ""

                output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/edit'>" % restrauntIDPath
                output += "<input name='updaterestraunt' type='text'>"
                output += "<input type='submit' value='Rename'> </form>"
                output += "</body></html>"
                self.wfile.write(output)
                editRestaurant = Restaurant(name="updaterestraunt")
                session.add(editRestaurant)
                session.commit()
                print output
                return
        except IOError:
                    pass


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print "Web server running on port %s" % port
        server.serve_forever()

    except KeyboardInterrupt:
        print "^C entered, stopping web server..."
        server.socket.close()

if __name__ == '__main__':
    main()
