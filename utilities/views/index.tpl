   <form action="choose">
    <h2>Please Choose Schema.org Type</h2>
    <input list="schema_types" name="schema_types">
    <datalist id="schema_types">
    % for row in schema_types:
      <option value="{{ row }}">
    % end
    </datalist>
    <input type="submit" />
   </form>
% rebase base
