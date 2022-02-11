package Model.value;

import Model.type.IType;

public interface IValue {
    IType get_type();
    IValue deep_copy();
    String toString();
    boolean equals(Object o);
}
