import { defineStore } from "pinia";

interface User {
  id: string;
  phone: string;
  username?: string;
}

export const useAuthStore = defineStore("auth", () => {
  const token = useCookie<string | null>("auth_token", {
    maxAge: 60 * 60 * 24 * 30,
    path: "/",
  });

  const user = ref<User | null>(null);
  const isAuthenticated = computed((): boolean => !!token.value);

  const loading = ref(false);
  const error = ref<string | null>(null);

  function setToken(newToken: string): void {
    token.value = newToken;
  }

  function setUser(userData: User): void {
    user.value = userData;
  }

  function logout(): void {
    token.value = null;
    user.value = null;
    navigateTo("/auth");
  }

  return { token, user, isAuthenticated, setToken, setUser, logout };
});
