import dva from 'dva';
import { Router, Route, Switch } from 'dva/router';
import styles from './index.less'
import {connect} from 'dva';
import key from 'keymaster';

// 1. Initialize
const app = dva();

// 2. Model

// model中定义数据state和数据处理函数reducers
app.model({
  namespace: 'counter',
  // 用来存放数据
  state: {
    record: 0,
    current: 0
  },

  // 用来处理异步请求
  // call表示调用异步函数，put表示调用dispatch
  effects: {
    *add(action, {call, put}) {
      yield call(delay, 1000);
      yield put({ type: 'minus' });
    }
  },

  // reducer的主要作用就是更改state
  // ？？参数是哪里来的
  reducers: {
    add(state) {
      const newCurrent = state.current + 1;
      return {...state,
        record: newCurrent > state.record ? newCurrent : state.record,
        current: newCurrent
      }
    }, 
    minus(state) {
      return { ...state,
        current: state.current - 1
      }
    }
  },
  // 订阅一个数据源，然后根据条件dispatch需要的action
  subscriptions: {
    keyboardWatcher({dispatch}) {
      key('⌘+up, ctrl+up', () => { dispatch({type: 'add'}); })
    }
  }
  
})

function delay(timeout){
  return new Promise(resolve => {
    setTimeout(resolve, timeout);
  });
}

// 在commponent中定义展示的view
// dispatch需要选择某一个namespace下的reducer
const CountApp = ( {counter, dispatch} ) => {
  return (
    <div className={styles.container}>      
      <div className={styles.record}>Highest Record{counter.record}</div>
      <div className={styles.current}>{counter.current}</div>
      <div className={styles.button}>
        <button onClick={()=>{ dispatch({type: 'counter/add'}); }}>+</button>
      </div>
    </div>
  );
}

// state有很多的namespace,其中一个是counter
// 把state.counter作为props传入component
// 这就是函数名mapStateToProps的意思
function mapStateToProps(state) {
  return {counter: state.counter};
}

// ??
const Homepage = connect(mapStateToProps)(CountApp);

// 3. Router
app.router(({ history }) =>
  <Router history={history}>
      <Route path="/" component={Homepage} />
  </Router>
);

// 4. Start
app.start('#root');
