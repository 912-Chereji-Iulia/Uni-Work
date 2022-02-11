package Model.type;

import Model.value.IValue;

public interface IType {
    IValue default_value();
    IType deep_copy();
    String toString();
}
