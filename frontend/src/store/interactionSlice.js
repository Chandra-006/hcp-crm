import { createSlice } from '@reduxjs/toolkit';

/**
 * Initial state for the interaction form data.
 */
const initialState = {
    hcp_name: '',
    interaction_type: 'Meeting', // Default value
    date: '',
    time: '',
    topics_discussed: '',
    sentiment: 'Neutral',
    materials_shared: ''
  };

/**
 * Redux slice for managing interaction form state.
 *
 * This slice handles updates to the interaction form fields,
 * typically triggered by the AI assistant extracting data from chat.
 */
const interactionSlice = createSlice({
  name: 'interaction',
  initialState,
  reducers: {
    // This is the function the AI will call to fill the form
    updateFields: (state, action) => {
      return { ...state, ...action.payload };
    },
  },
});

export const { updateFields } = interactionSlice.actions;
export default interactionSlice.reducer;