<script setup>
const isLoginPage = ref(true);

const isPasswordVisible = ref(false);

const togglePassword = () => {
  isPasswordVisible.value = !isPasswordVisible.value;
};

const number = ref("+7");
const password = ref("");

watch(number, (newVal, oldVal) => {
  if (!newVal.startsWith("+7")) {
    number.value = "+7";
    return;
  }

  const prefix = "+7";
  const body = newVal.slice(prefix.length);
  const onlyDigits = body.replace(/\D/g, "");

  if (body !== onlyDigits) {
    number.value = prefix + onlyDigits;
  }

  if (number.value.length > 12) {
    number.value = oldVal;
  }
});
</script>

<template>
  <div class="register">
    <div class="register__block">
      <h1 class="register__title">
        {{ isLoginPage ? "Вход" : "Регистрация" }}
      </h1>

      <input class="register__input" type="text" v-model="number" />

      <div class="register__password">
        <input
          v-model="password"
          class="register__input"
          :type="isPasswordVisible ? 'text' : 'password'"
          :placeholder="isLoginPage ? 'Введите пароль' : 'Придумайте пароль'"
        />
        <button type="button" @click="togglePassword" class="register__eye">
          <div></div>
        </button>
      </div>

      <p class="register__toggle" @click="isLoginPage = !isLoginPage">
        {{ isLoginPage ? "Ещё нет аккаунта?" : "Уже есть аккаунт?" }}
      </p>
      <button class="register__button">Продолжить</button>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.register {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100vh;
  color: $text-primary;

  &__block {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 80%;
  }
  &__title {
    font-size: 24px;
    margin: 0 0 20px 0;
  }
  &__input {
    width: 90%;
    height: 40px;
    border-radius: $border-radius;
    margin: 0 0 15px 0;
    padding: 0 40px 0 20px;
    border: 1px solid $accent;

    &:focus {
      outline: 1px solid $text-secondary;
      box-shadow: 0 0 2px $accent;
    }

    &::placeholder {
      color: $text-primary;
      opacity: 0.5;
      font-size: 12px;
      font-weight: 400;
    }
  }
  &__password {
    position: relative;
    width: 100%;
    display: flex;
    justify-content: center;
  }
  &__eye {
    position: absolute;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 40px;
    height: 40px;
    right: 5%;
    top: 0;

    & div {
      background-color: $text-primary;
      width: 22px;
      height: 22px;
      mask-image: url("/images/eye.svg");
      mask-repeat: no-repeat;
      mask-position: center;
      mask-size: contain;
      -webkit-mask-image: url("/images/eye.svg");
    }

    &:hover {
      & div {
        background-color: $accent;
      }
    }
  }
  &__toggle {
    font-size: 12px;
    align-self: flex-start;
    margin: 0 0 10px 7%;
    color: $text-secondary;
    cursor: pointer;
    user-select: none;
  }
  &__button {
    margin: 10px 0 0 0;
    &:hover {
      color: $text-secondary;
    }
  }
}
</style>
