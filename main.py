import pandas as pd
import numpy as np
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode

if 'df' not in st.session_state:
    st.session_state['df'] = pd.DataFrame(
        np.fromfunction(lambda i, j: i * 10 + j, (3,4), dtype=int),
        columns=["A", "B", "C", "D"],
        dtype=str
    )

# df2 - DataFrame to add new rows.
df2 = pd.DataFrame(
    np.fromfunction(lambda i, j: (100 + i) * 10 + j, (2,4), dtype=int),
    columns=["A", "B", "C", "D"],
    dtype=str
)


def main():
    global df2
    st.subheader('An example of adding and removing rows in st-aggrid.')
    st.write('To delete a row, check the checkbox at the beginning of the row.')

    js_del_selected_rows = JsCode("""
    function(e) {
        let api = e.api;        
        let sel = api.getSelectedRows();
        api.applyTransaction({remove: sel});
    };
    """)

    opt_builder = GridOptionsBuilder.from_dataframe(st.session_state['df'])
    opt_builder.configure_default_column(editable=True)
    opt_builder.configure_selection(selection_mode='multiple', use_checkbox=True)
    opt_builder.configure_grid_options(onRowSelected=js_del_selected_rows)
    grid_opt = opt_builder.build()
    ag_return = AgGrid(st.session_state['df'], grid_opt,
        fit_columns_on_grid_load=True, allow_unsafe_jscode=True)

    btn_add_rows = st.button('**Add rows**')
    if btn_add_rows:
        st.session_state['df'] = pd.concat([ag_return.data, df2], ignore_index=True)
        st.experimental_rerun()
    
    with st.expander('**Program source code**', False):
        code = '''
import pandas as pd
import numpy as np
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode

if 'df' not in st.session_state:
    st.session_state['df'] = pd.DataFrame(
        np.fromfunction(lambda i, j: i * 10 + j, (3,4), dtype=int),
        columns=["A", "B", "C", "D"],
        dtype=str
    )

# df2 - DataFrame to add new rows.
df2 = pd.DataFrame(
    np.fromfunction(lambda i, j: (100 + i) * 10 + j, (2,4), dtype=int),
    columns=["A", "B", "C", "D"],
    dtype=str
)


def main():
    global df2
    st.subheader('An example of adding and removing rows in st-aggrid.')
    st.write('To delete a row, check the checkbox at the beginning of the row.')

    js_del_selected_rows = JsCode("""
    function(e) {
        let api = e.api;        
        let sel = api.getSelectedRows();
        api.applyTransaction({remove: sel});
    };
    """)

    opt_builder = GridOptionsBuilder.from_dataframe(st.session_state['df'])
    opt_builder.configure_default_column(editable=True)
    opt_builder.configure_selection(selection_mode='multiple', use_checkbox=True)
    opt_builder.configure_grid_options(onRowSelected=js_del_selected_rows)
    grid_opt = opt_builder.build()
    ag_return = AgGrid(st.session_state['df'], grid_opt,
        fit_columns_on_grid_load=True, allow_unsafe_jscode=True)

    btn_add_rows = st.button('**Add rows**')
    if btn_add_rows:
        st.session_state['df'] = pd.concat([ag_return.data, df2], ignore_index=True)
        st.experimental_rerun()
    
    with st.expander('**Program source code**', False):
        code = """

        """
        st.code(code, language='python')


if __name__ == "__main__": 
    main()
        '''
        st.code(code, language='python')


if __name__ == "__main__": 
    main()