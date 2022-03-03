# from exceptions import Exception

def c3_lineration(kls):
    if len(kls.__bases__) == 1:
        return [kls, kls.__base__]
    else:
        l = [c3_lineration(base) for base in kls.__bases__]
        l.append([base for base in kls.__bases__])
        return [kls] + merge(l)

def merge(args):
    if args:
        for mro_list in args:
            for class_type in mro_list:
                for comp_list in args:
                    if class_type in comp_list[1:]:
                        break
                else:
                    next_merge_list = []
                    for arg in args:
                        if class_type in arg:
                            arg.remove(class_type)
                            if arg:
                                next_merge_list.append(arg)
                        else:
                            next_merge_list.append(arg)
                    return [class_type] + merge(next_merge_list)
        else:
            raise Exception
    else:
        return []



class A(object):pass
class B(object):pass
class C(object):pass
class E(A,B):pass
class F(B,C):pass
class G(E,F):pass

print (c3_lineration(G))

#-*- encoding:GBK -*-#
def mro_C3(*cls):
        if len(cls)==1:
            if not cls[0].__bases__:
                return  cls
            else:
                return cls+ mro_C3(*cls[0].__bases__)
        else:
            seqs = [list(mro_C3(C)) for C in cls ] +[list(cls)]
            res = []
            while True:
              non_empty = list(filter(None, seqs))
              if not non_empty:
                  return tuple(res)
              for seq in non_empty:
                  candidate = seq[0]
                  not_head = [s for s in non_empty if candidate in s[1:]]
                  if not_head:
                      candidate = None
                  else:
                      break
              if not candidate:
                  raise TypeError("inconsistent hierarchy, no C3 MRO is possible")
              res.append(candidate)
              for seq in non_empty:
                  if seq[0] == candidate:
                      del seq[0]