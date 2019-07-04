
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const webpack = require('webpack')

const clientConfig = {
  entry: {
    app: './src/index.js',
  },
  devtool: 'inline-source-map',
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'dist/'),
    publicPath: '/'
  },
  devServer: {
    contentBase: './',
    hot: true,
    publicPath: '/',
    proxy: {
      '/data': {
        target: 'http://localhost:3000/',
        secure: false,
        changeOrigin: true,
      }
    },
  },

  plugins: [
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      title: 'Learning'
    }),
    new webpack.NamedModulesPlugin(),
    new webpack.HotModuleReplacementPlugin(),
  ],
  module: {
    rules: [
      {
        test: /\.jpg$/,
        use: [{
          loader: 'file-loader',
          options: {
            limit: 10000,
            name: 'assets/img/[name].[ext]'
          }
        }],

      },
      {
        test: /\.css$/,
        use: ['style-loader',
          'css-loader']
      }
    ]
  }
}

module.exports = clientConfig