<div class="panel panel-default">
  <div class="panel-body">
    <div class="col-sm-offset-3 col-sm-8">
      <form action="/multiply" class="form-horizontal" method="get">
        <div class="form-group">
          <label for="multiplicand" class="col-sm-2 control-label"> Num 1: </label>
          <div class="col-sm-6">
            <input type="number" class="form-control" id="multiplicand"
                name="num1" placeholder="Enter a number" required>
          </div>
        </div>
        <div class="form-group">
          <label for="multiplier" class="col-sm-2 control-label"> Num 2: </label>
          <div class="col-sm-6">
            <input type="number" class="form-control" id="multiplier"
                name="num2" placeholder="Enter a number" required>
          </div>
        </div>
        <div class="form-group">
          <div class="col-sm-offset-4 col-sm-10">
            <button type="submit" class="btn btn-success"> Multiply </button>
          </div>
        </div>
      </form>
    </div>
  </div>
</div>
