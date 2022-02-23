from views import index, items, sync

def setup_routes(app):
  app.router.add_get('/', index) # Render HTML site
  app.router.add_get('/items', items) # Returns JSON items list
  app.router.add_post('/syncitems', sync) # Saves items to the server