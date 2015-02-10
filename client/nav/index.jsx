var defaultItems = [
{
  isActive: true,
  data: {
    action: '/',
    text: 'Home'
  },
  id: 0
},
{
  data: {
    action: '/login',
    text: 'Login / Sign Up'
  },
  id: 1
},
{
  data: {
    action: '/projects',
    text: 'Browse Projects'
  },
  id: 2
}]

module.exports = function getNavForPath(path) {
  items = defaultItems.map(function(item) {
    item.isActive = (item.data.action === path)
    return item
  })
  console.log('Items: ', items)
  return items
}