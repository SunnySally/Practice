const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const webpack = require('webpack')

module.exports = {
  entry: {
    app: './src/index.js',
  },
  devtool: 'inline-source-map',
  output: {
    chunkFilename: '[name].bundle.js',
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'dist'),
    publicPath: '/v1/'
  },
  devServer: {
    contentBase: './',
    hot: true,
    host: '127.0.0.1',
    port: 3000
  },
  plugins: [
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      title: 'Output Management'
    }),
    new webpack.NamedModulesPlugin(),
    new webpack.HotModuleReplacementPlugin(),
  ],
  module: {
    rules: [
      {
        test: /\.jpg$/,
        use: ['file-loader']
      },
      {
        test: /\.css$/,
        use: ['style-loader',
          'css-loader']
      }
    ]
  },
  // optimization: {
  //   splitChunks: {
  //     chunks: 'async', 
  //     minSize: 30000,
  //     maxSize: 0,
  //     minChunks: 1,
  //     maxAsyncRequests: 5,
  //     maxInitialRequests: 3,
  //     automaticNameDelimiter: '~',
  //     name: true,
  //     cacheGroups: {
  //       common: {
  //         test: /[\\/]node_modules[\\/]/,
  //         name: 'common',
  //         chunks: 'initial',
  //         priority: 2,
  //         minChunks: 2,
  //       },
  //       default: {
  //         minChunks: 2,
  //         priority: -20,
  //         reuseExistingChunk: true
  //       }
  //     }
  //   }
  // }
};

