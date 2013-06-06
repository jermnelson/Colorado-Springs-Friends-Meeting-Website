<div class="container">
   <form action="choose">
    <h2>Please Choose Schema.org Type</h2>
    <input list="schema_types" name="schema_types">
    <datalist id="schema_types">
    % for row in schema_types:
      <option value="{{ row }}">
    % end
    </datalist>
    <input type="submit" class="btn btn-primary" />
   </form>
   <form action="update_config">
    <h3>Location of JSON LD files</h3>
    <input type="text" class="span3" name="location">
    <input type="submit" class="btn">
   </form>
</div>
% rebase base
