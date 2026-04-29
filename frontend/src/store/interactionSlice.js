import { createSlice } from '@reduxjs/toolkit';

const initialState = {
    hcp_name: '',
    interaction_type: 'Meeting', // Default value
    date: '',
    time: '',
    topics_discussed: '',
    sentiment: 'Neutral',
    materials_shared: ''
  };

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