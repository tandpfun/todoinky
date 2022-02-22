from views import index, items, sync

def setup_routes(app):
  app.router.add_get('/', index)
  app.router.add_get('/items', items)
  app.router.add_post('/syncitems', sync)