const rules = {
  'max-len': ['error', 80, 2, { ignoreUrls: true }],
  'no-console': [0],
  'no-restricted-syntax': 'off',
  'no-continue': 'off',
  'no-underscore-dangle': 'off',
  'import/extensions': 'off',
  'import/no-unresolved': 'off',
  'operator-linebreak': 'off',
  'implicit-arrow-linebreak': 'off',
  'react/destructuring-assignment': 'off',
  'jsx-a11y/click-events-have-key-events': 'off',
  'jsx-a11y/no-static-element-interactions': 'off',
  'react/jsx-one-expression-per-line': 'off',
  'no-use-before-define': 'off',
  '@typescript-eslint/no-use-before-define': ['error'],
  camelcase: 'off',
  'react/jsx-filename-extension': [2, { extensions: ['.ts', '.tsx'] }],
  'lines-between-class-members': [
    'error',
    'always',
    { exceptAfterSingleLine: true },
  ],
};

module.exports = {
  extends: [
    'airbnb',
    'prettier',
    'eslint:recommended',
    'plugin:react/recommended',
    'plugin:import/errors',
    'plugin:react/recommended',
    'plugin:@typescript-eslint/recommended',
  ],
  parser: '@typescript-eslint/parser',
  rules,
  env: {
    browser: true,
    commonjs: true,
    node: true,
    jest: true,
    es6: true,
  },
  plugins: ['react', 'react-hooks', 'jsx-a11y'],
  settings: {
    ecmascript: 6,
    jsx: true,
    'import/resolver': {
      node: {
        paths: ['src'],
      },
    },
    'import/parsers': {
      '@typescript-eslint/parser': ['.ts', '.tsx'],
    },
    react: {
      pragma: 'React',
      version: '16.8',
    },
  },
};
