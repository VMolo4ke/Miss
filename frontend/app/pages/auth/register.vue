<script setup>
const number = ref("+7");

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
      <h1 class="register__title">Регистрация</h1>
      <input class="register__input" type="text" v-model="number" />
      <input
        class="register__input"
        type="password"
        placeholder="Придумайте пароль"
      />
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
    padding: 0 0 0 20px;
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
  &__button {
    margin: 10px 0 0 0;
    &:hover {
      color: $text-secondary;
    }
  }
}
</style>
