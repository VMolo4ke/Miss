export default defineNuxtRouteMiddleware((to, from) => {
  const authStore = useAuthStore()
  const token = useCookie("auth_token").value;
  const authPage = "/auth";

  const publicPath = [authPage, '/docs']

  const isPublicPath = publicPath.some(path => to.path.startsWith(path))

  if (!authStore.isAuthenticated && !isPublicPath) {
    return navigateTo(authPage)
  }

  if (authStore.isAuthenticated && to.path === authPage) {
    return navigateTo('/')
  }
});
