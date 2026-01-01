export default defineNuxtRouteMiddleware((to, from) => {
  const token = useCookie("auth_token").value;
  const authPage = "/auth";

  if (!token && to.path !== authPage) {
    return navigateTo(authPage);
  }

  if (token && to.path === authPage) {
    return navigateTo("/");
  }
});
