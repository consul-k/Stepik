class Animal
{
    public $kind;
    public $name;

    function viewData() {
        echo $this->kind, $this->name;
    }
}
