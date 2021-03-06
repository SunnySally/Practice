const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin')
const webpack = require('webpack')

module.exports = {
  // entry: './src/index.js',
  entry: {
    app: './src/index.js',
    // print: './src/print.js'
  },
  devtool: 'inline-source-map',
  devServer: {
    contentBase: './', //用来指定
    hot: true
  },
  plugins: [
    new CleanWebpackPlugin(['dist']),
    new HtmlWebpackPlugin({
      title: 'output management'
    }),
    new webpack.HotModuleReplacementPlugin()
  ],
  output: {
    // filename: 'main.js',
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'dist'),
    publicPath: '/public/'
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          'style-loader',
          'css-loader'
        ]
      },
      //     {
      //       test: /\.(gif|png|svg|jpg)$/,
      //       use: [
      //         'file-loader'
      //       ]
      //     },
      //     {
      //       test: /\.(woff|woff2|eot|ttf|otf)$/,
      //       use: [
      //         'file-loader'
      //       ]
      //     },
      //     {
      //       test: /\.(csv|tsv)$/,
      //       use: [
      //         'csv-loader'
      //       ]
      //     },
      //     {
      //       test: /\.xml$/,
      //       use: [
      //         'xml-loader'
      //       ]
      //     }
    ]
  }
};